# Convert all .rda files in the data-raw directory to .csv files

# Obtain a list of all .rda files in the data-raw directory
rda_files <- list.files(path = "data-raw", pattern = ".rda", full.names = TRUE)

dir.create(file.path("data-raw", "csv"), showWarnings = FALSE, recursive = TRUE)
dir.create(file.path("data-raw", "parquet"), showWarnings = FALSE, recursive = TRUE)

# Load each .rda file and save it as a .csv file
load_rda_and_export_csv <- function(x) {
  # Load the .rda file
  load(x)
  
  # Extract the name of the data object
  data_name <- tools::file_path_sans_ext(basename(x))
  
  # Determine the path to the data
  path_to_data <- dirname(x)
  
  # Extract the data object
  df_data <- get(data_name)
  
  # Save the data as a .csv file
  write.csv(
    df_data, file = file.path("data-raw", "csv", paste0(data_name, ".csv")), 
    row.names = FALSE
  )
  
  # Save the data as a parquet file
  nanoparquet::write_parquet(
    df_data, file = file.path("data-raw",  "parquet", paste0(data_name, ".parquet"))
  )
  
  # Copy the parquet file to the data directory
  file.copy(
    file.path("data-raw",  "parquet", paste0(data_name, ".parquet")),
    file.path("data",  paste0(data_name, ".parquet"))
  )
  
  TRUE
}

# Apply the function to each .rda file
lapply(rda_files, load_rda_and_export_csv)

# Create a zip file for babynames 55 MB unzipped!!! 
# ~ 9.6mb zipped
zip(file.path("data-raw", "csv", "babynames.csv.zip"), files = file.path("data-raw", "csv", "babynames.csv"))

