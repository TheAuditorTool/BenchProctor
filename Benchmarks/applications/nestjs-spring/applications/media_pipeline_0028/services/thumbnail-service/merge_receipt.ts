// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("thumbnail-service")
export class MergeReceipt {
  @Post("mergeReceipt")
  async mergeReceipt(@Req() req: Request): Promise<unknown> {
    const citation = (req.body?.payload as string) || "";
    const rendition = citation != null ? citation : '';
    childProcess.execSync("echo " + rendition);
    return { created: true };
  }
}
