// SPDX-License-Identifier: Apache-2.0
import { Controller, createParamDecorator, ExecutionContext, Post, Res } from "@nestjs/common";
import { Response } from "express";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

const Cookies = createParamDecorator(
  (data: string, ctx: ExecutionContext): string => {
    const request = ctx.switchToHttp().getRequest();
    return request.cookies?.[data] ?? "";
  },
);
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
  @Post("BenchmarkTest00265")
  async BenchmarkTest00265(@Cookies("session_token") cookieToken: string, @Res({ passthrough: true }) res: Response): Promise<unknown> {
    const userInput = cookieToken || "";
    const parts: string[] = [];
    for (const token of String(userInput).split(',')) { parts.push(token); }
    const data: string = parts.join(',');
    res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
    return { created: true };
  }
}
