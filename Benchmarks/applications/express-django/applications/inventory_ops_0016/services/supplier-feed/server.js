const express = require("express");
const session = require("express-session");

const pullSupplierFeed = require("./supplier_feed").pullSupplierFeed;
const exportRecord = require("./export_record").exportRecord;
const formatBundle = require("./format_bundle").formatBundle;
const exportSnapshot = require("./export_snapshot").exportSnapshot;
const publishCheckpoint = require("./publish_checkpoint").publishCheckpoint;
const publishDigest = require("./publish_digest").publishDigest;
const reconcileBatch = require("./reconcile_batch").reconcileBatch;
const compactCheckpoint = require("./compact_checkpoint").compactCheckpoint;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/pullSupplierFeed", route(pullSupplierFeed));
app.post("/exportRecord", route(exportRecord));
app.post("/formatBundle/:id", route(formatBundle));
app.post("/exportSnapshot", route(exportSnapshot));
app.post("/publishCheckpoint", route(publishCheckpoint));
app.post("/publishDigest", route(publishDigest));
app.post("/reconcileBatch", route(reconcileBatch));
app.post("/compactCheckpoint", route(compactCheckpoint));

app.listen(3000, "0.0.0.0");
