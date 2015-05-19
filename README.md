# Alteryx_Filters
Python Script to extract filters and formulas used in alteryx workflows.

Alteryx Workflows are stored as an yxmd file which can be opened as XML. Sometimes we need to document all the filters and formulas used in the workflows. It is literally not possible to open each workflow and capture these filters. This python code is used to parse the XML for filter and formula configuration in each workflow and store them in a csv.

This will reduce lot of manual work required during documentation or workflow upgrades.

Note :- All filters and formula functions are captured here. It can be extended to capture all the functions used in developing the workflow. 
