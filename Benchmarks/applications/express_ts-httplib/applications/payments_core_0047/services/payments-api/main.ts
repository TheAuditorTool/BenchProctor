import express, { Request, Response } from "express";
import session from "express-session";

import { authorizePayment } from "./payment_authorize";
import { annotateSnapshot } from "./annotate_snapshot";
import { auditReport } from "./audit_report";
import { summarizeManifest } from "./summarize_manifest";
import { validateConfig } from "./validate_config";
import { publishPolicy } from "./publish_policy";
import { enrichWallet } from "./enrich_wallet";
import { mergeDigest } from "./merge_digest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/authorizePayment/:id", authorizePayment);
app.post("/annotateSnapshot", annotateSnapshot);
app.post("/auditReport", auditReport);
app.post("/summarizeManifest", summarizeManifest);
app.post("/validateConfig", validateConfig);
app.post("/publishPolicy", publishPolicy);
app.post("/enrichWallet", enrichWallet);
app.post("/mergeDigest", mergeDigest);

app.listen(3000, "0.0.0.0");
