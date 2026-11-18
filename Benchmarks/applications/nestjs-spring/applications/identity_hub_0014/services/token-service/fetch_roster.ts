// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("token-service")
export class FetchRoster {
  @Post("fetchRoster")
  async fetchRoster(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers.authorization as string) || "";
    const tokens = String(snippet).split(',').filter((t) => t.length > 0);
    const persona = tokens.join(' ');
    childProcess.execFileSync("echo", [persona]);
    return { created: true };
  }
}
