from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from superagi.models.cluster_agent import ClusterAgent
from superagi.models.cluster_configuration import ClusterConfiguration
from superagi.models.base_model import DBBaseModel
from superagi.models.db import connect_db

engine = connect_db()
Session = sessionmaker(bind=engine)


class Cluster(DBBaseModel):
    """
       Represents an cluster entity.

       Attributes:
           id (int): The unique identifier of the cluster.
           name (str): The name of the cluster.
           project_id (int): The identifier of the associated project.
           description (str): The description of the cluster.
       """

    __tablename__ = 'clusters'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    project_id = Column(Integer)
    description = Column(String)

    def __repr__(self):
        """
        Returns a string representation of the Cluster object.

        Returns:
            str: String representation of the Cluster.

        """
        return f"Cluster(id={self.id}, name='{self.name}', project_id={self.project_id}, " \
               f"description='{self.description}')"

    @classmethod
    def get_cluster_by_id(cls, cluster_id: int):
        """
        Fetches the cluster for the given cluster id.

        Args:
            cluster_id (int): The identifier of the cluster.

        Returns:
            Cluster: The cluster object.
        """
        session = Session()
        cluster = session.query(cls).filter(cls.id == cluster_id).first()
        session.close()
        return cluster

    @classmethod
    def get_clusters_by_project_id(cls, project_id: int):
        """
        Fetches the clusters for the given project id.

        Args:
            project_id (int): The identifier of the project.

        Returns:
            list: List of clusters.
        """
        session = Session()
        cluster = session.query(cls).filter(cls.project_id == project_id).all()
        session.close()
        return cluster

    @staticmethod
    def create_cluster(cluster_name: str, project_id: int, description: str):
        """
        Creates a cluster with the given name, project id and description.
        Args:
            cluster_name (str): The name of the cluster.
            project_id (int): The identifier of the associated project.
            description (str): The description of the cluster.

        Returns:
            Cluster: The cluster object.
        """
        session = Session()
        cluster = Cluster(name=cluster_name, project_id=project_id, description=description)
        session.add(cluster)
        session.commit()
        session.close()
        return cluster

    @staticmethod
    def create_cluster_with_config(cluster_name: str, project_id: int, description: str, agent_ids: [int], config: dict):
        """
        Creates a cluster with the given name, project id, description and config dict.
        Args:
            cluster_name (str): The name of the cluster.
            project_id (int): The identifier of the associated project.
            description (str): The description of the cluster.
            agent_ids (list): The list of agent ids associated with the cluster.
            config (dict): The configuration of the cluster.

        Returns:
            Cluster: The cluster object.
        """
        session = Session()
        cluster = Cluster(name=cluster_name, project_id=project_id, description=description)
        session.add(cluster)
        session.commit()
        session.close()
        cluster_id = cluster.id
        ClusterConfiguration.create_cluster_config(cluster_id, config)
        ClusterAgent.create_cluster_agents(cluster_id, agent_ids)
        return cluster

