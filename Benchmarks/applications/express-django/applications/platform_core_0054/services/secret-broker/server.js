const express = require("express");
const session = require("express-session");

const fetchSecret = require("./secret_fetch").fetchSecret;
const buildReceipt = require("./build_receipt").buildReceipt;
const rotateSummary = require("./rotate_summary").rotateSummary;
const compactSecret = require("./compact_secret").compactSecret;
const rotateConfig = require("./rotate_config").rotateConfig;
const publishSecret = require("./publish_secret").publishSecret;
const reconcileThreshold = require("./reconcile_threshold").reconcileThreshold;
const mergeRecord = require("./merge_record").mergeRecord;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/fetchSecret", route(fetchSecret));
app.post("/buildReceipt/:id", route(buildReceipt));
app.post("/rotateSummary", route(rotateSummary));
app.post("/compactSecret", route(compactSecret));
app.post("/rotateConfig", route(rotateConfig));
app.post("/publishSecret", route(publishSecret));
app.post("/reconcileThreshold", route(reconcileThreshold));
app.post("/mergeRecord", route(mergeRecord));

app.listen(3000, "0.0.0.0");
