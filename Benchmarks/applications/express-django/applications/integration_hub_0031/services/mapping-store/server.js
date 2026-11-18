const express = require("express");
const session = require("express-session");

const mapField = require("./field_mapping").mapField;
const summarizeHeader = require("./summarize_header").summarizeHeader;
const validateMapping = require("./validate_mapping").validateMapping;
const summarizeThreshold = require("./summarize_threshold").summarizeThreshold;
const fetchSummary = require("./fetch_summary").fetchSummary;
const collectReport = require("./collect_report").collectReport;
const archiveWebhook = require("./archive_webhook").archiveWebhook;
const summarizeWebhook = require("./summarize_webhook").summarizeWebhook;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/mapField", route(mapField));
app.post("/summarizeHeader", route(summarizeHeader));
app.post("/validateMapping", route(validateMapping));
app.post("/summarizeThreshold", route(summarizeThreshold));
app.post("/fetchSummary", route(fetchSummary));
app.post("/collectReport", route(collectReport));
app.post("/archiveWebhook", route(archiveWebhook));
app.post("/summarizeWebhook", route(summarizeWebhook));

app.listen(3000, "0.0.0.0");
