const express = require("express");
const session = require("express-session");

const declareCustoms = require("./customs_declare").declareCustoms;
const fetchConfig = require("./fetch_config").fetchConfig;
const compactBundle = require("./compact_bundle").compactBundle;
const auditDigest = require("./audit_digest").auditDigest;
const pruneManifest = require("./prune_manifest").pruneManifest;
const rotateThreshold = require("./rotate_threshold").rotateThreshold;
const fetchCarrier = require("./fetch_carrier").fetchCarrier;
const annotateHeader = require("./annotate_header").annotateHeader;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/declareCustoms", route(declareCustoms));
app.post("/fetchConfig", route(fetchConfig));
app.post("/compactBundle", route(compactBundle));
app.post("/auditDigest", route(auditDigest));
app.post("/pruneManifest", route(pruneManifest));
app.post("/rotateThreshold", route(rotateThreshold));
app.post("/fetchCarrier", route(fetchCarrier));
app.post("/annotateHeader", route(annotateHeader));

app.listen(3000, "0.0.0.0");
