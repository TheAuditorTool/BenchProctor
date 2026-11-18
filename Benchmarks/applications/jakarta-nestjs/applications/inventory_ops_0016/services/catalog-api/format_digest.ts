// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("catalog-api")
export class FormatDigest {
  @Post("formatDigest")
  async formatDigest(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.authorization as string) || "";
    const parts: string[] = [];
    for (const token of String(citation).split(',')) { parts.push(token); }
    const backorder: string = parts.join(',');
    childProcess.execFileSync("echo", [backorder]);
    return { created: true };
  }
}
