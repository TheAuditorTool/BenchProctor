const express = require("express");
const session = require("express-session");

const renderThumbnail = require("./thumbnail_render").renderThumbnail;
const mergeReceipt = require("./merge_receipt").mergeReceipt;
const normalizeReceipt = require("./normalize_receipt").normalizeReceipt;
const collectPolicy = require("./collect_policy").collectPolicy;
const resolvePolicy = require("./resolve_policy").resolvePolicy;
const collectRecord = require("./collect_record").collectRecord;
const renderAsset = require("./render_asset").renderAsset;
const pruneCheckpoint = require("./prune_checkpoint").pruneCheckpoint;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/renderThumbnail", renderThumbnail);
app.post("/mergeReceipt/:id", mergeReceipt);
app.post("/normalizeReceipt", normalizeReceipt);
app.post("/collectPolicy", collectPolicy);
app.post("/resolvePolicy", resolvePolicy);
app.post("/collectRecord", collectRecord);
app.post("/renderAsset", renderAsset);
app.post("/pruneCheckpoint", pruneCheckpoint);

app.listen(3000, "0.0.0.0");
