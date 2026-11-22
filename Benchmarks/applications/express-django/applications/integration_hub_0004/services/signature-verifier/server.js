const express = require("express");
const session = require("express-session");

const verifySignature = require("./signature_verify").verifySignature;
const reconcileSummary = require("./reconcile_summary").reconcileSummary;
const summarizeLedger = require("./summarize_ledger").summarizeLedger;
const rotateLedger = require("./rotate_ledger").rotateLedger;
const validateBatch = require("./validate_batch").validateBatch;
const fetchPolicy = require("./fetch_policy").fetchPolicy;
const enrichReport = require("./enrich_report").enrichReport;
const renderManifest = require("./render_manifest").renderManifest;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/verifySignature", route(verifySignature));
app.post("/reconcileSummary", route(reconcileSummary));
app.post("/summarizeLedger", route(summarizeLedger));
app.post("/rotateLedger", route(rotateLedger));
app.post("/validateBatch", route(validateBatch));
app.post("/fetchPolicy", route(fetchPolicy));
app.post("/enrichReport", route(enrichReport));
app.post("/renderManifest", route(renderManifest));

app.listen(3000, "0.0.0.0");
