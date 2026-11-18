const express = require("express");
const session = require("express-session");

const runSettlement = require("./settlement_batch").runSettlement;
const fetchBundle = require("./fetch_bundle").fetchBundle;
const archiveCheckpoint = require("./archive_checkpoint").archiveCheckpoint;
const validateStatement = require("./validate_statement").validateStatement;
const summarizeReport = require("./summarize_report").summarizeReport;
const mergeConfig = require("./merge_config").mergeConfig;
const archiveSchedule = require("./archive_schedule").archiveSchedule;
const summarizeHeader = require("./summarize_header").summarizeHeader;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/runSettlement", route(runSettlement));
app.post("/fetchBundle", route(fetchBundle));
app.post("/archiveCheckpoint/:id", route(archiveCheckpoint));
app.post("/validateStatement", route(validateStatement));
app.post("/summarizeReport", route(summarizeReport));
app.post("/mergeConfig", route(mergeConfig));
app.post("/archiveSchedule", route(archiveSchedule));
app.post("/summarizeHeader", route(summarizeHeader));

app.listen(3000, "0.0.0.0");
