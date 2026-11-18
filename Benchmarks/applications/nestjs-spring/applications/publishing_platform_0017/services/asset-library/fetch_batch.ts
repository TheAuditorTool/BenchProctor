// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("asset-library")
export class FetchBatch {
  @Post("fetchBatch")
  async fetchBatch(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.payload as string) || "";
    const tokens = String(summary).split(',').filter((t) => t.length > 0);
    const addendum = tokens.join(' ');
    childProcess.execSync("echo " + addendum);
    return { created: true };
  }
}
