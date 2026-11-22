// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("index-builder")
export class AuditWindow {
  @Post("auditWindow")
  async auditWindow(@Req() req: Request): Promise<unknown> {
    const citation = (req.body as string) || "";
    const [dossier] = String(citation).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(dossier)) { throw new ForbiddenException({error:'forbidden'}); }
    const addendum = dossier;
    childProcess.spawn("echo " + addendum, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
