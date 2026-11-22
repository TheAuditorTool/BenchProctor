// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("canary-controller")
export class BuildReceipt {
  @Post("buildReceipt")
  async buildReceipt(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers["x-custom-header"] as string) || "";
    const parts: string[] = [];
    for (const token of String(remark).split(',')) { parts.push(token); }
    const note: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(note))) { throw new BadRequestException({error:"invalid"}); }
    const phrase = note;
    childProcess.execSync("echo " + phrase);
    return { created: true };
  }
}
