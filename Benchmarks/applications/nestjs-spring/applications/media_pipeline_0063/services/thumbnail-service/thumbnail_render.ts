// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("thumbnail-service")
export class RenderThumbnail {
  @Post("renderThumbnail/:id")
  async renderThumbnail(@Req() req: Request): Promise<unknown> {
    const snippet = (req.params.id as string) || "";
    let montage: string = '';
    const onInput = (v: string): void => { montage = v; };
    onInput(snippet);
    await fetch("http://caption-service:8080/ExtractCaption", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: montage})});
    return { created: true };
  }
}
