const express = require("express");
const session = require("express-session");

const postLedgerEntry = require("./ledger_post").postLedgerEntry;
const mergeReport = require("./merge_report").mergeReport;
const rotateLedger = require("./rotate_ledger").rotateLedger;
const pruneSummary = require("./prune_summary").pruneSummary;
const normalizeInvoice = require("./normalize_invoice").normalizeInvoice;
const enrichManifest = require("./enrich_manifest").enrichManifest;
const validateSummary = require("./validate_summary").validateSummary;
const collectHeader = require("./collect_header").collectHeader;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/postLedgerEntry", postLedgerEntry);
app.post("/mergeReport", mergeReport);
app.post("/rotateLedger", rotateLedger);
app.post("/pruneSummary", pruneSummary);
app.post("/normalizeInvoice", normalizeInvoice);
app.post("/enrichManifest", enrichManifest);
app.post("/validateSummary", validateSummary);
app.post("/collectHeader", collectHeader);

app.listen(3000, "0.0.0.0");
