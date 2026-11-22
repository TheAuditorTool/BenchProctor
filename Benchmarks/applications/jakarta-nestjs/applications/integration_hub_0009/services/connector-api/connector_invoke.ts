// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("connector-api")
export class InvokeConnector {
  @Post("invokeConnector")
  async invokeConnector(@Req() req: Request): Promise<unknown> {
    const quotation = req.body.integrations_payload || "";
    childProcess.execSync("echo " + quotation);
    return { created: true };
  }
}
