// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, StreamableFile } from "@nestjs/common";
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
  @Post("BenchmarkTest00101")
  async BenchmarkTest00101(@Headers("user-agent") ua: string): Promise<unknown> {
    const userInput = ua || "";
    const _raw = userInput;
    const data = (_raw && _raw.length > 0) ? _raw : 'default';
    const processed = isoDompurify.sanitize(marked.parse(data) as string);
    return new StreamableFile(Buffer.from("<section>" + processed + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
