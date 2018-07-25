# Copyright (c) 2018, WSO2 Inc. (http://wso2.com) All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

NS = {'d': 'http://maven.apache.org/POM/4.0.0'}
ZIP_FILE_EXTENSION = ".zip"
VALUE_TAG = "{http://maven.apache.org/POM/4.0.0}value"
DATASOURCE_PATHS = ["conf/broker.yaml"]
DIST_POM_PATH = {"ballerina-message-broker": "modules/launcher/pom.xml"}
LIB_PATH = "lib"
DISTRIBUTION_PATH = "modules/distribution/product/target"
PRODUCT_STORAGE_DIR_NAME = "storage"
TEST_PLAN_PROPERTY_FILE_NAME = "testplan-props.properties"
INFRA_PROPERTY_FILE_NAME = "infrastructure.properties"
LOG_FILE_NAME = "integration.log"
ORACLE_DB_ENGINE = "ORACLE-SE2"
MYSQL_DB_ENGINE = "MYSQL"
DEFAULT_ORACLE_SID = "orcl"
MB_DB = 'MB_DB'
DEFAULT_DB_USERNAME = "wso2carbon"
DB_META_DATA = {
    "MYSQL": {"prefix": "jdbc:mysql://", "driverClassName": "com.mysql.jdbc.Driver", "jarName": "mysql.jar"},
    "SQLSERVER-SE": {"prefix": "jdbc:sqlserver://",
                     "driverClassName": "com.microsoft.sqlserver.jdbc.SQLServerDriver", "jarName": "sqlserver-ex.jar"},
    "ORACLE-SE2": {"prefix": "jdbc:oracle:thin:@", "driverClassName": "oracle.jdbc.OracleDriver",
                   "jarName": "oracle-se.jar"},
    "POSTGRESQL": {"prefix": "jdbc:postgresql://", "driverClassName": "org.postgresql.Driver",
                   "jarName": "postgres.jar"}
}
