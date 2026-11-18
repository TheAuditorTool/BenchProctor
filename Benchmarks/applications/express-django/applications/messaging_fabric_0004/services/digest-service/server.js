const express = require("express");
const session = require("express-session");

const rollDigest = require("./digest_roll").rollDigest;
const verifySchedule = require("./verify_schedule").verifySchedule;
const annotateProfile = require("./annotate_profile").annotateProfile;
const validateBatch = require("./validate_batch").validateBatch;
const verifySubscription = require("./verify_subscription").verifySubscription;
const rotateDelivery = require("./rotate_delivery").rotateDelivery;
const verifyPolicy = require("./verify_policy").verifyPolicy;
const compactBatch = require("./compact_batch").compactBatch;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/rollDigest/:id", route(rollDigest));
app.post("/verifySchedule", route(verifySchedule));
app.post("/annotateProfile", route(annotateProfile));
app.post("/validateBatch", route(validateBatch));
app.post("/verifySubscription", route(verifySubscription));
app.post("/rotateDelivery", route(rotateDelivery));
app.post("/verifyPolicy", route(verifyPolicy));
app.post("/compactBatch", route(compactBatch));

app.listen(3000, "0.0.0.0");
