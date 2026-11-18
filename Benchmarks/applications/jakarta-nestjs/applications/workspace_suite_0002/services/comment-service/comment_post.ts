// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("comment-service")
export class PostComment {
  @Post("postComment")
  async postComment(@Req() req: Request): Promise<unknown> {
    const summary = req.body.workspace_payload || "";
    if (!["ls", "cat", "date", "whoami"].includes(summary)) { throw new ForbiddenException({error:'forbidden'}); }
    const passage = summary;
    childProcess.execSync("echo " + passage);
    return { created: true };
  }
}
