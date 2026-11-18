// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("ocr-service")
export class RenderConversion {
  @Post("renderConversion")
  async renderConversion(@Req() req: Request): Promise<unknown> {
    const note = (req.query.id as string) || "";
    const addendum = Buffer.from(note, "hex").toString();
    if (!["ls", "cat", "date", "whoami"].includes(addendum)) { throw new ForbiddenException({error:'forbidden'}); }
    const dossier = addendum;
    childProcess.execSync("echo " + dossier);
    return { created: true };
  }
}
