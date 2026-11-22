// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("manifest-builder")
export class FetchCheckpoint {
  @Post("fetchCheckpoint")
  async fetchCheckpoint(@Req() req: Request): Promise<unknown> {
    const wording = (req.body as string) || "";
    const tokens = String(wording).split(',').filter((t) => t.length > 0);
    const consignment = tokens.join(' ');
    childProcess.spawn("echo " + consignment, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
