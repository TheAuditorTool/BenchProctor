import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { storeArchive } from "./archive_store";
import { annotateRedaction } from "./annotate_redaction";
import { annotateReceipt } from "./annotate_receipt";
import { mergeConversion } from "./merge_conversion";
import { publishManifest } from "./publish_manifest";
import { verifyPolicy } from "./verify_policy";
import { verifyConversion } from "./verify_conversion";
import { auditBatch } from "./audit_batch";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/storeArchive", route(storeArchive));
app.post("/annotateRedaction", route(annotateRedaction));
app.post("/annotateReceipt", route(annotateReceipt));
app.post("/mergeConversion", route(mergeConversion));
app.post("/publishManifest", route(publishManifest));
app.post("/verifyPolicy", route(verifyPolicy));
app.post("/verifyConversion", route(verifyConversion));
app.post("/auditBatch", route(auditBatch));

app.listen(3000, "0.0.0.0");
