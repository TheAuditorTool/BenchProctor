import express, { Request, Response } from "express";
import session from "express-session";

import { checkSla } from "./sla_check";
import { pruneReceipt } from "./prune_receipt";
import { resolveSnapshot } from "./resolve_snapshot";
import { rotateCheckpoint } from "./rotate_checkpoint";
import { verifyRoster } from "./verify_roster";
import { renderCheckpoint } from "./render_checkpoint";
import { prunePolicy } from "./prune_policy";
import { fetchManifest } from "./fetch_manifest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/checkSla", checkSla);
app.post("/pruneReceipt", pruneReceipt);
app.post("/resolveSnapshot", resolveSnapshot);
app.post("/rotateCheckpoint", rotateCheckpoint);
app.post("/verifyRoster/:id", verifyRoster);
app.post("/renderCheckpoint", renderCheckpoint);
app.post("/prunePolicy", prunePolicy);
app.post("/fetchManifest/:id", fetchManifest);

app.listen(3000, "0.0.0.0");
