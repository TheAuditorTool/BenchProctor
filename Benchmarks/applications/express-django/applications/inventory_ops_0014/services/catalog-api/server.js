const express = require("express");
const session = require("express-session");

const lookupSku = require("./sku_lookup").lookupSku;
const archiveHeader = require("./archive_header").archiveHeader;
const enrichHeader = require("./enrich_header").enrichHeader;
const loadBatch = require("./load_batch").loadBatch;
const renderLedger = require("./render_ledger").renderLedger;
const resolveAllocation = require("./resolve_allocation").resolveAllocation;
const rotateDigest = require("./rotate_digest").rotateDigest;
const reconcileSummary = require("./reconcile_summary").reconcileSummary;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/lookupSku", route(lookupSku));
app.post("/archiveHeader", route(archiveHeader));
app.post("/enrichHeader", route(enrichHeader));
app.post("/loadBatch", route(loadBatch));
app.post("/renderLedger", route(renderLedger));
app.post("/resolveAllocation", route(resolveAllocation));
app.post("/rotateDigest", route(rotateDigest));
app.post("/reconcileSummary", route(reconcileSummary));

app.listen(3000, "0.0.0.0");
