const express = require("express");
const session = require("express-session");

const runConversion = require("./convert_job").runConversion;
const annotateBundle = require("./annotate_bundle").annotateBundle;
const normalizeSnapshot = require("./normalize_snapshot").normalizeSnapshot;
const rotateReceipt = require("./rotate_receipt").rotateReceipt;
const fetchThreshold = require("./fetch_threshold").fetchThreshold;
const buildCheckpoint = require("./build_checkpoint").buildCheckpoint;
const annotateHeader = require("./annotate_header").annotateHeader;
const reconcileBundle = require("./reconcile_bundle").reconcileBundle;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/runConversion", route(runConversion));
app.post("/annotateBundle/:id", route(annotateBundle));
app.post("/normalizeSnapshot", route(normalizeSnapshot));
app.post("/rotateReceipt", route(rotateReceipt));
app.post("/fetchThreshold", route(fetchThreshold));
app.post("/buildCheckpoint", route(buildCheckpoint));
app.post("/annotateHeader", route(annotateHeader));
app.post("/reconcileBundle", route(reconcileBundle));

app.listen(3000, "0.0.0.0");
