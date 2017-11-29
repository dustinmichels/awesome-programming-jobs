import pandas as pd


########################
# Define some global vars
########################

OUTFILE = 'README.md'

HEADER = "# Awesome Programming Jobs \
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n\
\nA curated list of awesome companies using technology & computer science \
to confront pressing social and environmental issues.\n\
\nInspired by [awesome-python](https://github.com/vinta/awesome-python) \
and other [awesome lists](https://github.com/sindresorhus/awesome).\n\n"

# This gets filled in by npm package 'doctoc'
CONTENTS = "## Contents\n\
\n<!-- START doctoc -->\n\
<!-- END doctoc -->\n\
\n---\n\n"

SYMBOL_DICT = {
    'Clean Energy':':sunny:',
    'Smart Agriculture':':seedling:',
    'Smart Cities':':vertical_traffic_light:'
}


########################
# Load CSV
########################

df = pd.read_csv('jobs.csv')
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df.sort_values(by='topic', inplace=True)


########################
# Write to README.md
########################

def write_job_type(topic):
    if topic in SYMBOL_DICT:
        symbol = SYMBOL_DICT[topic]
    else:
        symbol = ''

    return f'\n## {topic} {symbol}\n\n'


def write_job_descriptions(row):
    company_info = '* **[{}]({})** : **{}** - {}\n'.format(
        row.company_name,
        row.website,
        row.location,
        row.description)
    print(company_info)
    return company_info


def create_readme():
    """
    Read csv, render markdown
    """

    f = open(OUTFILE, 'w')

    f.write(HEADER)
    f.write(CONTENTS)

    # For job type headers and job descriptions
    for topic in df['topic'].unique():
        f.write(write_job_type(topic))
        topic_df = df[df['topic'] == topic]
        for row in topic_df.itertuples():
            f.write(write_job_descriptions(row))
    f.close()


create_readme()
