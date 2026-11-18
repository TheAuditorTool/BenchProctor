// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("transcode-service")
export class MergeIndex {
  @Post("mergeIndex")
  async mergeIndex(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers.authorization as string) || "";
    const _raw = notice;
    const rendition = (_raw && _raw.length > 0) ? _raw : 'default';
    nodeSerialize.unserialize(rendition);
    return { created: true };
  }
}
