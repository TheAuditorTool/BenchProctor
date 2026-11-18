const express = require("express");
const session = require("express-session");

const shipLog = require("./log_ship").shipLog;
const validateReceipt = require("./validate_receipt").validateReceipt;
const validateBundle = require("./validate_bundle").validateBundle;
const loadSummary = require("./load_summary").loadSummary;
const compactThreshold = require("./compact_threshold").compactThreshold;
const fetchIndex = require("./fetch_index").fetchIndex;
const enrichRecord = require("./enrich_record").enrichRecord;
const normalizeSchedule = require("./normalize_schedule").normalizeSchedule;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/shipLog", route(shipLog));
app.post("/validateReceipt/:id", route(validateReceipt));
app.post("/validateBundle", route(validateBundle));
app.post("/loadSummary", route(loadSummary));
app.post("/compactThreshold", route(compactThreshold));
app.post("/fetchIndex", route(fetchIndex));
app.post("/enrichRecord", route(enrichRecord));
app.post("/normalizeSchedule", route(normalizeSchedule));

app.listen(3000, "0.0.0.0");
