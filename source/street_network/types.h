#include "type/type.h"

#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/adj_list_serialize.hpp>
#include <boost/serialization/serialization.hpp>
#include <boost/serialization/vector.hpp>
#include <boost/serialization/utility.hpp>

#include <unordered_map>
#include <map>

namespace bg = boost::graph;
namespace nt = navitia::type;
namespace navitia { namespace streetnetwork {

/** Propriétés Nœud (intersection entre deux routes) */
struct Vertex {
    double lon;
    double lat;

    template<class Archive> void serialize(Archive & ar, const unsigned int) {
        ar & lon & lat;
    }
};

/** Propriétés des arcs */
struct Edge {
    nt::idx_t way_idx; //< indexe vers le nom de rue
    float length; //< longeur en mètres de l'arc
    bool cyclable; //< est-ce que le segment est accessible à vélo ?
    int start_number; //< numéro de rue au début du segment
    int end_number; //< numéro de rue en fin de segment

    template<class Archive> void serialize(Archive & ar, const unsigned int) {
        ar & way_idx & length & cyclable & start_number & end_number;
    }
};

// Plein de typedefs pour nous simpfilier un peu la vie

/** Définit le type de graph que l'on va utiliser
  *
  * Les arcs sortants et la liste des nœuds sont représentés par des vecteurs
  * les arcs sont orientés
  * les propriétés des nœuds et arcs sont les classes définies précédemment
  */
typedef boost::adjacency_list<boost::vecS, boost::vecS, boost::directedS, Vertex, Edge> Graph;

/// Représentation d'un nœud dans le graphe
typedef boost::graph_traits<Graph>::vertex_descriptor vertex_t;

/// Représentation d'un arc dans le graphe
typedef boost::graph_traits<Graph>::edge_descriptor edge_t;

/// Type Itérateur sur les nœuds du graphe
typedef boost::graph_traits<Graph>::vertex_iterator vertex_iterator;

/// Type itérateur sur les arcs du graphe
typedef boost::graph_traits<Graph>::edge_iterator edge_iterator;

/** Nommage d'une voie (anciennement "adresse"). Typiquement le nom de rue **/
struct Way{
    nt::idx_t idx;
    std::string name;
    std::string city;
    nt::idx_t city_idx;
    std::vector< std::pair<vertex_t, vertex_t> > edges;


    template<class Archive> void serialize(Archive & ar, const unsigned int) {
        ar & idx & name & city & edges;
    }
};

/** Un bout d'itinéraire : un nom de voie et une liste de segments */
struct PathItem{
    nt::idx_t way_idx; //< Voie sur laquel porte le bout du trajet
    float length; //< Longueur du trajet effectué sur cette voie
    std::vector<nt::idx_t> segments; //< Segments traversés
    PathItem() : length(0){}
};

/** Itinéraire complet */
struct Path {
    float length; //< Longueur totale du parcours
    std::vector<PathItem> path_items; //< Liste des voies parcourues
    std::vector<nt::GeographicalCoord> coordinates; //< Coordonnées du parcours
};

struct StreetNetwork {
    std::vector<Way> ways;
    std::vector<nt::City> cities;
    Graph graph;

    ///map temporaire pour la correspondance way => city
    std::map<std::string, nt::idx_t> city_map;

    void load_bdtopo(std::string filename);
    void load_bdcity(std::string filename);
    void load_bd(const std::string& path);

    template<class Archive> void serialize(Archive & ar, const unsigned int) {
        ar & ways & graph;
    }


    void save(const std::string & filename);
    void load(const std::string & filename);

    void save_bin(const std::string & filename);
    void load_bin(const std::string & filename);

    void load_flz(const std::string & filename);
    void save_flz(const std::string & filename);

    /// Calcule le meilleur itinéraire entre deux listes de nœuds
    Path compute(std::vector<vertex_t> starts, std::vector<vertex_t> destinations);


};

}} //namespace navitia::streetnetwork