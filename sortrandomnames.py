from quick_sort import quicksort
from binary_search import binary_search

names = [
    "James Martinez", "John Davis", "Jennifer Johnson", "Elizabeth Martinez", "John Johnson",
    "John Martinez", "James Brown", "Elizabeth Davis", "Jennifer Smith", "Jennifer Johnson",
    "James Smith", "James Johnson", "James Johnson", "Elizabeth Miller", "Elizabeth Martinez",
    "John Smith", "James Smith", "John Miller", "Jennifer Johnson", "Jennifer Smith",
    "James Jones", "Jennifer Davis", "John Miller", "John Brown", "Elizabeth Martinez",
    "John Miller", "Elizabeth Miller", "John Martinez", "Elizabeth Smith", "Jennifer Martinez",
    "Jennifer Davis", "Linda Martinez", "James Johnson", "Elizabeth Davis", "James Miller",
    "Jennifer Smith", "John Johnson", "Linda Miller", "John Johnson", "Linda Davis",
    "James Brown", "James Williams", "Jennifer Davis", "Linda Davis", "James Martinez",
    "Linda Miller", "John Brown", "Elizabeth Martinez", "Jennifer Williams", "Linda Smith",
    "James Miller", "Jennifer Martinez", "Linda Johnson", "John Williams", "Jennifer Miller",
    "James Smith", "John Smith", "Linda Davis", "Jennifer Brown", "Linda Johnson",
    "Jennifer Smith", "James Williams", "Linda Williams", "Elizabeth Martinez", "John Williams",
    "James Jones", "James Smith", "Linda Smith", "Linda Smith", "James Jones", "John Johnson",
    "Jennifer Martinez", "Elizabeth Martinez", "Jennifer Smith", "Linda Brown",
    "Jennifer Williams", "Linda Smith", "James Johnson", "John Smith", "Linda Johnson",
    "James Williams", "James Jones", "Jennifer Davis", "Jennifer Miller", "Linda Johnson",
    "Elizabeth Martinez", "John Miller", "James Williams", "Linda Johnson", "Elizabeth Miller",
    "Jennifer Miller", "John Martinez", "John Miller", "Linda Williams", "James Williams",
    "John Jones", "Linda Jones", "Jennifer Miller", "James Johnson", "Linda Williams",
    "Linda Jones"
]

sorted_names = quicksort(names)
targetValue = binary_search(sorted_names, "Linda Johnson")

print("My target was found at Index: ", targetValue)
