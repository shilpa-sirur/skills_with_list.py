"""
Prints out all the melons in our inventory
"""

from melons import melons



def print_all_melons(melons_data):
	for melon, metadata in melons_data.items():
		print "The type of melon is : ", melon
		melon.upper()
		for metadata, value in metadata.items():
		    print "%s : %s" % (metadata,value)
		         	
print_all_melons(melons)
