const express = require("express");
const session = require("express-session");

const lookupOrder = require("./order_lookup").lookupOrder;
const verifyWindow = require("./verify_window").verifyWindow;
const archivePolicy = require("./archive_policy").archivePolicy;
const resolveBundle = require("./resolve_bundle").resolveBundle;
const enrichReport = require("./enrich_report").enrichReport;
const validateThreshold = require("./validate_threshold").validateThreshold;
const compactRoster = require("./compact_roster").compactRoster;
const verifyOrder = require("./verify_order").verifyOrder;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/lookupOrder", route(lookupOrder));
app.post("/verifyWindow", route(verifyWindow));
app.post("/archivePolicy", route(archivePolicy));
app.post("/resolveBundle", route(resolveBundle));
app.post("/enrichReport", route(enrichReport));
app.post("/validateThreshold", route(validateThreshold));
app.post("/compactRoster", route(compactRoster));
app.post("/verifyOrder", route(verifyOrder));

app.listen(3000, "0.0.0.0");
