import express, { Request, Response } from "express";
import session from "express-session";

import { transformPayload } from "./payload_transform";
import { reconcileLedger } from "./reconcile_ledger";
import { compactConnector } from "./compact_connector";
import { resolveCheckpoint } from "./resolve_checkpoint";
import { archivePolicy } from "./archive_policy";
import { resolveDigest } from "./resolve_digest";
import { formatRecord } from "./format_record";
import { exportBatch } from "./export_batch";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/transformPayload", transformPayload);
app.post("/reconcileLedger", reconcileLedger);
app.post("/compactConnector", compactConnector);
app.post("/resolveCheckpoint", resolveCheckpoint);
app.post("/archivePolicy", archivePolicy);
app.post("/resolveDigest", resolveDigest);
app.post("/formatRecord", formatRecord);
app.post("/exportBatch", exportBatch);

app.listen(3000, "0.0.0.0");
