# Convert all .rda files in the data-raw directory to .csv files

# Obtain a list of all .rda files in the data-raw directory
rda_files <- list.files(path = "data-raw/rda", pattern = ".rda", full.names = TRUE)

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
    row.names = FALSE, fileEncoding = "UTF-8"
  )
  
  # Save the data as a parquet file
  nanoparquet::write_parquet(
    df_data, file = file.path("data-raw",  "parquet", paste0(data_name, ".parquet"))
  )
  
  file.copy(
    file.path("data-raw", "parquet", paste0(data_name, ".parquet")),
    file.path("pybabynames", "data", paste0(data_name, ".parquet")),
    overwrite = TRUE
  )
  
  TRUE
}

# Apply the function to each .rda file
lapply(rda_files, load_rda_and_export_csv)

# Create a zip file for babynames 55 MB unzipped!!! 
# ~ 9.6mb zipped
oldwd <- setwd(file.path("data-raw", "csv"))
zip("babynames.csv.zip", files = "babynames.csv")
setwd(oldwd)

