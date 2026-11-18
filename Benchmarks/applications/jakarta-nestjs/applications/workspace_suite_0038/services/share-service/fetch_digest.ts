// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("share-service")
export class FetchDigest {
  @Post("fetchDigest")
  async fetchDigest(@Req() req: Request): Promise<unknown> {
    const preface = (req.body.multipart_field as string) || "";
    const remark = preface != null ? preface : '';
    JSON.parse(remark);
    return { created: true };
  }
}
