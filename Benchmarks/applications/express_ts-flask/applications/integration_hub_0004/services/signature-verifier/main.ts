import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { verifySignature } from "./signature_verify";
import { reconcileSummary } from "./reconcile_summary";
import { summarizeLedger } from "./summarize_ledger";
import { rotateLedger } from "./rotate_ledger";
import { validateBatch } from "./validate_batch";
import { fetchPolicy } from "./fetch_policy";
import { enrichReport } from "./enrich_report";
import { renderManifest } from "./render_manifest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/verifySignature", verifySignature);
app.post("/reconcileSummary", reconcileSummary);
app.post("/summarizeLedger", summarizeLedger);
app.post("/rotateLedger", rotateLedger);
app.post("/validateBatch", validateBatch);
app.post("/fetchPolicy", fetchPolicy);
app.post("/enrichReport/:id", enrichReport);
app.post("/renderManifest", renderManifest);

app.listen(3000, "0.0.0.0");
