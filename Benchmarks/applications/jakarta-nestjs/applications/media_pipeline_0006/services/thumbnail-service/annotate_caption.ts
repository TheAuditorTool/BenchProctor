// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("thumbnail-service")
export class AnnotateCaption {
  @Post("annotateCaption")
  async annotateCaption(@Req() req: Request): Promise<unknown> {
    const passage = (req.body.multipart_field as string) || "";
    const montage = passage != null ? passage : '';
    JSON.parse(montage);
    return { created: true };
  }
}
