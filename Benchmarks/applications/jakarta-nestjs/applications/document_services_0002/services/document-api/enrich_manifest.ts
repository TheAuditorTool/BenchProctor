// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("document-api")
export class EnrichManifest {
  @Post("enrichManifest")
  async enrichManifest(@Req() req: Request): Promise<unknown> {
    const wording = (req.body as string) || "";
    const [addendum] = String(wording).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(addendum)) { throw new ForbiddenException({error:'forbidden'}); }
    const dossier = addendum;
    childProcess.spawn("echo " + dossier, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
