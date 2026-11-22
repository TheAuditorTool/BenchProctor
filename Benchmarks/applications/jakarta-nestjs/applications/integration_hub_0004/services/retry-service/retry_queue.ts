// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("retry-service")
export class QueueRetry {
  @Post("queueRetry")
  async queueRetry(@Req() req: Request): Promise<unknown> {
    const citation = req.body.integrations_payload || "";
    childProcess.execFileSync("echo", [citation]);
    return { created: true };
  }
}
