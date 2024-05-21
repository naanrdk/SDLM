class Term:
  """Represents a business term within the semantic layer."""

  def __init__(self, name, definition, data_source_mappings=[]):
    self.name = name
    self.definition = definition
    self.data_source_mappings = data_source_mappings  # List of mappings to source data

  def add_data_source_mapping(self, data_source, field_name):
    """Maps the term to a specific field in a data source."""
    self.data_source_mappings.append({"source": data_source, "field": field_name})

class SDLA:
  """Core functionalities for building and managing a semantic data layer."""

  def __init__(self):
    self.terms = {}  # Dictionary of Term objects (term name -> Term)

  def define_term(self, name, definition):
    """Defines a new business term in the semantic layer."""
    if name in self.terms:
      raise ValueError(f"Term '{name}' already exists")
    self.terms[name] = Term(name, definition)

  def map_term_to_data(self, term_name, data_source, field_name):
    """Maps a business term to a specific field in a data source."""
    if term_name not in self.terms:
      raise ValueError(f"Term '{term_name}' not found")
    self.terms[term_name].add_data_source_mapping(data_source, field_name)

  def search_terms(self, search_query):
    """Searches for relevant terms based on a user query (placeholder)."""
    # Implement logic to search term names, definitions, and data source mappings
    # for matches with the search query
    matching_terms = []
    for term in self.terms.values():
      if search_query.lower() in term.name.lower() or search_query.lower() in term.definition.lower():
        matching_terms.append(term)
    return matching_terms

  def get_data_source_mappings(self, term_name):
    """Retrieves data source mappings for a specific term."""
    if term_name not in self.terms:
      raise ValueError(f"Term '{term_name}' not found")
    return self.terms[term_name].data_source_mappings

def main():
  # Create a SDLA instance
  sdla = SDLA()

  # Define business terms (replace with actual terms and definitions)
  sdla.define_term("Customer Revenue", "Total revenue generated from a customer")
  sdla.define_term("Product Sales", "Number of units of a product sold")

  # Map terms to data sources (replace with actual data source mappings)
  sdla.map_term_to_data("Customer Revenue", "Sales Database", "customer_revenue")
  sdla.map_term_to_data("Product Sales", "Sales Database", "product_sales")

  # Simulate searching for terms
  search_query = "customer income"
  matching_terms = sdla.search_terms(search_query)
  if matching_terms:
    print(f"\nSearch Results for '{search_query}':")
    for term in matching_terms:
      print(f"- {term.name} ({term.definition})")
  else:
    print(f"\nNo terms found matching '{search_query}'.")

  # Simulate retrieving data source mappings
  term_name = "Customer Revenue"
  mappings = sdla.get_data_source_mappings(term_name)
  if mappings:
    print(f"\nData Source Mappings for '{term_name}':")
    for mapping in mappings:
      print(f"- {mapping['source']}: {mapping['field']}")
  else:
    print(f"\nNo data source mappings found for '{term_name}'.")

if __name__ == "__main__":
  main()
