// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("metadata-index")
export class IndexMetadata {
  @Post("indexMetadata")
  async indexMetadata(@Req() req: Request): Promise<unknown> {
    const heading = req.body.media_payload || "";
    childProcess.execSync("echo " + heading);
    return { created: true };
  }
}
