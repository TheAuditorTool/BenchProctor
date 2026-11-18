// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("survey-service")
export class FetchHeader {
  @Post("fetchHeader")
  async fetchHeader(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.authorization as string) || "";
    const parts: string[] = [];
    for (const token of String(remark).split(',')) { parts.push(token); }
    const inquiry: string = parts.join(',');
    childProcess.execFileSync("echo", [inquiry]);
    return { created: true };
  }
}
