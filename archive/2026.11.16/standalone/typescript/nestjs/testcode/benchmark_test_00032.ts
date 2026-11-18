// SPDX-License-Identifier: Apache-2.0
import { Controller, Header, Headers, Post } from "@nestjs/common";
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
  @Post("BenchmarkTest00032")
  @Header("Content-Type", "text/html")
  async BenchmarkTest00032(@Headers("authorization") auth: string): Promise<unknown> {
    const userInput = auth || "";
    const _raw = userInput;
    const data = (_raw && _raw.length > 0) ? _raw : 'default';
    const processed = isoDompurify.sanitize(marked.parse(data) as string);
    return "<div>" + processed + "</div>";
  }
}
