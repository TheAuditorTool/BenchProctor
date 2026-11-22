const express = require("express");
const session = require("express-session");

const saveRevision = require("./revision_save").saveRevision;
const mergeReceipt = require("./merge_receipt").mergeReceipt;
const resolveManifest = require("./resolve_manifest").resolveManifest;
const enrichArticle = require("./enrich_article").enrichArticle;
const compactSnapshot = require("./compact_snapshot").compactSnapshot;
const resolveHeader = require("./resolve_header").resolveHeader;
const renderRecord = require("./render_record").renderRecord;
const pruneRevision = require("./prune_revision").pruneRevision;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/saveRevision", route(saveRevision));
app.post("/mergeReceipt/:id", route(mergeReceipt));
app.post("/resolveManifest/:id", route(resolveManifest));
app.post("/enrichArticle", route(enrichArticle));
app.post("/compactSnapshot", route(compactSnapshot));
app.post("/resolveHeader", route(resolveHeader));
app.post("/renderRecord", route(renderRecord));
app.post("/pruneRevision", route(pruneRevision));

app.listen(3000, "0.0.0.0");
