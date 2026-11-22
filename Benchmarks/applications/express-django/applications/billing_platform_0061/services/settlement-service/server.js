const express = require("express");
const session = require("express-session");

const runSettlement = require("./settlement_batch").runSettlement;
const enrichManifest = require("./enrich_manifest").enrichManifest;
const loadRecord = require("./load_record").loadRecord;
const enrichInvoice = require("./enrich_invoice").enrichInvoice;
const normalizeSummary = require("./normalize_summary").normalizeSummary;
const renderDunning = require("./render_dunning").renderDunning;
const auditProfile = require("./audit_profile").auditProfile;
const enrichRecord = require("./enrich_record").enrichRecord;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/runSettlement", route(runSettlement));
app.post("/enrichManifest", route(enrichManifest));
app.post("/loadRecord", route(loadRecord));
app.post("/enrichInvoice", route(enrichInvoice));
app.post("/normalizeSummary", route(normalizeSummary));
app.post("/renderDunning", route(renderDunning));
app.post("/auditProfile", route(auditProfile));
app.post("/enrichRecord", route(enrichRecord));

app.listen(3000, "0.0.0.0");
