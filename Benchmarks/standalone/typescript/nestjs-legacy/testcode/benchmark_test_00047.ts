// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Query, StreamableFile } from "@nestjs/common";
import { Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00047")
  async BenchmarkTest00047(@Query("id") id: string): Promise<unknown> {
    const userInput = id || "";
    const data = String(userInput).replace(/\u0000/g, "");
    const processed = isoDompurify.sanitize(marked.parse(data) as string);
    return new StreamableFile(Buffer.from("<section>" + processed + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
