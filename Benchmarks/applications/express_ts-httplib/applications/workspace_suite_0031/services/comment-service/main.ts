import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { postComment } from "./comment_post";
import { reconcileManifest } from "./reconcile_manifest";
import { reconcileComment } from "./reconcile_comment";
import { pruneWorkspace } from "./prune_workspace";
import { reconcileDigest } from "./reconcile_digest";
import { compactReport } from "./compact_report";
import { mergeLedger } from "./merge_ledger";
import { validateComment } from "./validate_comment";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/postComment", route(postComment));
app.post("/reconcileManifest", route(reconcileManifest));
app.post("/reconcileComment", route(reconcileComment));
app.post("/pruneWorkspace", route(pruneWorkspace));
app.post("/reconcileDigest", route(reconcileDigest));
app.post("/compactReport", route(compactReport));
app.post("/mergeLedger", route(mergeLedger));
app.post("/validateComment", route(validateComment));

app.listen(3000, "0.0.0.0");
