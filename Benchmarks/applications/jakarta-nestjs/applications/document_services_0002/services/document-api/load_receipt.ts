// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("document-api")
export class LoadReceipt {
  @Post("loadReceipt")
  async loadReceipt(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers["x-custom-header"] as string) || "";
    const parts: string[] = [];
    for (const token of String(wording).split(',')) { parts.push(token); }
    const addendum: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(addendum))) { throw new BadRequestException({error:"invalid"}); }
    const dossier = addendum;
    childProcess.execSync("echo " + dossier);
    return { created: true };
  }
}
